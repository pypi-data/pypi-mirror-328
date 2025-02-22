# Copyright 2024 The Orbax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines free-function interface for saving."""

# pylint: disable=protected-access

import threading

from etils import epath
import orbax.checkpoint as ocp
from orbax.checkpoint.experimental.v1._src.path import types as path_types
from orbax.checkpoint.experimental.v1._src.synchronization import types as async_types
from orbax.checkpoint.experimental.v1._src.tree import types as tree_types


def _get_concurrent_gb(concurrent_bytes: int | None) -> int | None:
  if concurrent_bytes:
    return max(int(concurrent_bytes / 1e9), 1)
  return None


def save_pytree(
    directory: path_types.PathLike,
    pytree: tree_types.PyTreeOf[tree_types.LeafType],
    *,
    # Generic arguments.
    force: bool = False,
    custom_metadata: ocp.tree.JsonType | None = None,
    # PyTree-specific arguments.
    use_ocdbt: bool = True,
    use_zarr3: bool = True,
    save_concurrent_bytes: int | None = None,
    ocdbt_target_data_file_size: int | None = None,
    enable_pinned_host_transfer: bool = False,
):
  """Saves a PyTree.

  The operation blocks until complete. For improved performance, consider using
  `save_async` instead.

  Args:
    directory: The directory to save the checkpoint to.
    pytree: The PyTree to save. This may be any JAX PyTree (including custom
      objects registered as PyTrees) consisting of supported leaf types.
      Default supported leaf types include `jax.Array`,
      `np.ndarray`, simple types like `int`, `float`, `str`, and empty nodes.
      Support for custom leaves is also possible by implementing a
      `LeafTypeHandler`.
    force: Whether to allow the save to proceed even if it would fully overwrite
      an existing checkpoint.
    custom_metadata: User-provided custom metadata. An arbitrary
      JSON-serializable dictionary the user can use to store additional
      information. The field is treated as opaque by Orbax.
    use_ocdbt: Whether to use OCDBT for saving.
    use_zarr3: Whether to use Zarr3 for saving.
    save_concurrent_bytes: The maximum number of bytes to save concurrently.
    ocdbt_target_data_file_size: Specifies the target size (in bytes) of each
      OCDBT data file.  It only applies when OCDBT is enabled and Zarr3 must be
      turned on.  If left unspecified, default size is 2GB.  A value of 0
      indicates no maximum file size limit.  For best results, ensure
      chunk_byte_size is smaller than this value.  For more details, refer to
      https://google.github.io/tensorstore/kvstore/ocdbt/index.html#json-kvstore/ocdbt.target_data_file_size
    enable_pinned_host_transfer: If False, disables transfer to pinned host when
      copying from device to host, regardless of the presence of pinned host
      memory.
  """

  handler_registry = ocp.handlers.create_default_handler_registry(
      pytree=ocp.PyTreeCheckpointHandler(
          use_ocdbt=use_ocdbt,
          use_zarr3=use_zarr3,
          save_concurrent_gb=_get_concurrent_gb(save_concurrent_bytes),
      )
  )
  ckptr = ocp.Checkpointer(
      ocp.CompositeCheckpointHandler(handler_registry=handler_registry)
  )
  args = ocp.args.Composite(
      pytree=ocp.args.PyTreeSave(
          pytree,
          ocdbt_target_data_file_size=ocdbt_target_data_file_size,
          enable_pinned_host_transfer=enable_pinned_host_transfer,
      )
  )
  ckptr.save(directory, args=args, force=force, custom_metadata=custom_metadata)


class _SaveResponse(async_types.AsyncResponse[None]):
  """An `AsyncResponse` representing the result of `save_pytree_async`.

  TODO(cpgaffney): Note that a memory leak is possible if the user does not
  call `result`.
  """

  def __init__(self, checkpointer: ocp.AsyncCheckpointer):
    self._checkpointer = checkpointer
    self._thread = threading.Thread(target=self._wait_for_save)
    self._thread.start()

  def _wait_for_save(self):
    self._checkpointer.wait_until_finished()

  def result(self, timeout: int | None = None) -> None:
    self._thread.join()
    self._checkpointer.close()


def save_pytree_async(
    directory: path_types.PathLike,
    pytree: tree_types.PyTreeOf[tree_types.LeafType],
    *,
    # Generic arguments.
    force: bool = False,
    custom_metadata: ocp.tree.JsonType | None = None,
    # PyTree-specific arguments.
    use_ocdbt: bool = True,
    use_zarr3: bool = True,
    save_concurrent_bytes: int | None = None,
    ocdbt_target_data_file_size: int | None = None,
    enable_pinned_host_transfer: bool = False,
) -> async_types.AsyncResponse[None]:
  """Saves a PyTree asynchronously.

  Unlike `save`, this function returns immediately after the save operation is
  scheduled (except for certain operations, like device-to-host copying of
  on-device arrays, which must happen on the main thread). Further writing
  operations continue in a background thread. An `AsyncResponse` is returned
  that can be used to block until the save is complete (using
  `response.result()`). Make sure to wait for completion before attempting to
  load the checkpoint or exiting the program.

  Args:
    directory: The directory to save the checkpoint to.
    pytree: The PyTree to save. This may be any JAX PyTree (including custom
      objects registered as PyTrees) consisting of supported leaf types.
      Default supported leaf types include `jax.Array`,
      `np.ndarray`, simple types like `int`, `float`, `str`, and empty nodes.
      Support for custom leaves is also possible by implementing a
      `LeafTypeHandler`.
    force: Whether to allow the save to proceed even if it would fully overwrite
      an existing checkpoint.
    custom_metadata: User-provided custom metadata. An arbitrary
      JSON-serializable dictionary the user can use to store additional
      information. The field is treated as opaque by Orbax.
    use_ocdbt: Whether to use OCDBT for saving.
    use_zarr3: Whether to use Zarr3 for saving.
    save_concurrent_bytes: The maximum number of bytes to save concurrently.
    ocdbt_target_data_file_size: Specifies the target size (in bytes) of each
      OCDBT data file.  It only applies when OCDBT is enabled and Zarr3 must be
      turned on.  If left unspecified, default size is 2GB.  A value of 0
      indicates no maximum file size limit.  For best results, ensure
      chunk_byte_size is smaller than this value.  For more details, refer to
      https://google.github.io/tensorstore/kvstore/ocdbt/index.html#json-kvstore/ocdbt.target_data_file_size
    enable_pinned_host_transfer: If False, disables transfer to pinned host when
      copying from device to host, regardless of the presence of pinned host
      memory.

  Returns:
    An `AsyncResponse` that can be used to block until the save is complete.
    Blocking can be done using `response.result()`, which returns `None`.
  """


  handler_registry = ocp.handlers.create_default_handler_registry(
      pytree=ocp.PyTreeCheckpointHandler(
          use_ocdbt=use_ocdbt,
          use_zarr3=use_zarr3,
          save_concurrent_gb=_get_concurrent_gb(save_concurrent_bytes),
      )
  )
  ckptr = ocp.AsyncCheckpointer(
      ocp.CompositeCheckpointHandler(handler_registry=handler_registry)
  )
  args = ocp.args.Composite(
      pytree=ocp.args.PyTreeSave(
          pytree,
          ocdbt_target_data_file_size=ocdbt_target_data_file_size,
          enable_pinned_host_transfer=enable_pinned_host_transfer,
      )
  )
  directory = epath.Path(directory)
  ckptr.save(directory, args=args, force=force, custom_metadata=custom_metadata)
  return _SaveResponse(ckptr)
