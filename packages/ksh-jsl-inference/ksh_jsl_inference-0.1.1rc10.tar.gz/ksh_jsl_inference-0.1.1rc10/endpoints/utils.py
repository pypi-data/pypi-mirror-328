import sys
import threading
from typing import List, Union, Dict
from endpoints.log_utils import logger


def append_string_or_list_of_string(text: Union[str, List], texts: List) -> List[str]:
    if isinstance(text, str):
        texts.append(text)
    elif isinstance(text, list):
        texts.extend(text)
    return texts


def get_attr_or_key(item, key):
    """Fetches an attribute or dictionary key from an item."""
    return getattr(item, key, None) if hasattr(item, key) else item.get(key, None)


def copy_and_replace(src: str, dest: str, replacements: Dict[str, str]) -> None:
    """Copy a file from src to dest and replace the placeholders."""
    with open(src, "r") as f:
        content = f.read()
    for key, value in replacements.items():
        content = content.replace(key, value)
    with open(dest, "w") as f:
        f.write(content)


def generate_license_file(output_dir: str) -> None:
    """Generate a license file."""

    logger.debug(f"Generating license file in: {output_dir}")
    with open(f"{output_dir}/LICENSE", "w+") as f:
        f.write(
            """
Copyright 2015-2025 © John Snow Labs Inc.

This Software ("Software" or "Product") including code, design, documentation, configuration, models, tests, and related assets is owned by John Snow Labs Inc. All rights reserved.

John Snow Labs Inc. ("we") is the only owner of the copyright for this Software.

Unless otherwise specified in a separate Software License Agreement, Services Agreement, or End User License Agreement that you have executed directly with John Snow Labs Inc.:

* You are NOT granted any license or right to use the Software in any way.
* You are NOT granted any license or right to retain a copy of this Software.
* You are NOT granted any license or right to change, modify, adapt, or translate the Software.
* You are NOT granted any license or right to sell, assign, rent, exchange, lend, lease, sublease, or redistribute the Software.
* You are NOT granted any license or rights to bundle, repackage, or include the Software with any software in any way.
* The Software is Confidential and Proprietary. You are NOT allowed to distribute copies of the Software to others by any means whatsoever.
* The Software does NOT come with any warranty, express or implied.
* It is NOT legal to create derivative works based on the Software.
* It is NOT legal to claim any title in the Software or any of its derivatives.
* It is NOT legal to reverse engineer, disassemble or decompile the Software.
* It is NOT legal to make or retain a copy of the Software.
* We have no liability whatsoever for use of the Software.
* You may not make any public statements about this Software or John Snow Labs without explicit written permission from John Snow Labs.
* You must retain a copy of this notice without changes along with every copy of the Software, even if you have a license for it.

Unless required by applicable law or agreed to in writing, John Snow Labs provides the Software on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Software and assume any risks associated with Your exercise of permissions under this license.

In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall John Snow Labs be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this license or out of the use or inability to use the Software (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if advised of the possibility of such damages.

Unless required by applicable law or agreed to in writing, Software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. """
        )


class ProgressPercentage:
    def __init__(self, total_size):
        """
        Initialize the progress tracker.

        :param total_size: Total size of the file in bytes.
        """
        self._total_size = total_size
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def _update_progress(self, bytes_amount, operation):
        """
        Internal method to update and display progress.

        :param bytes_amount: Number of bytes processed in the current chunk.
        :param operation: Type of operation ("uploading" or "downloading").
        """
        with self._lock:
            self._seen_so_far += bytes_amount
            percent = (self._seen_so_far / self._total_size) * 100
            sys.stdout.write(f"\r{operation.capitalize()}... {percent:.2f}% complete")
            sys.stdout.flush()

    def upload_callback(self, bytes_amount):
        """
        Callback method for upload progress.

        :param bytes_amount: Number of bytes uploaded in the current chunk.
        """
        self._update_progress(bytes_amount, operation="uploading")

    def download_callback(self, bytes_amount):
        """
        Callback method for download progress.

        :param bytes_amount: Number of bytes downloaded in the current chunk.
        """
        self._update_progress(bytes_amount, operation="downloading")

