#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
# Copyright (c) 2020 starry69 & Contributors.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module to execute python code & bash commands in runtime"""


import subprocess, os, sys
from pyrogram import filters
from html import escape
from botname import botname, pfx, owner


@botname.on_message(filters.user(owner) & filters.command("exec", pfx))
def execute(client, msg):
    """
    Executes python programs dynamically
    in runtime.
    """

    code = msg.text.split(None, 1)[1]
    command = "".join(f"\n {x}" for x in code.split("\n.strip()"))

    res = subprocess.run(
        [sys.executable, "-c", command.strip()],
        capture_output=True,
        text=True,
        check=False,
    )
    result = str(res.stdout + res.stderr)

    if len(result) > 2000:
        with open("output.txt", "w+") as f:
            f.write(result)
        msg.reply_document(open("output.txt", "rb"))
        os.remove("output.txt")
    else:
        try:
            msg.edit_text("<pre>" + escape(result) + "</pre>")
        except Exception as excp:
            msg.edit_text(str(excp))


@botname.on_message(filters.user(owner) & filters.command("sh", pfx))
def shell(client, msg):
    """
    To execute terminal commands via bot
    """
    msg.edit_text("Running cmd...")
    try:
        res = subprocess.Popen(
            msg.command[1:],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = res.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())
        msg.edit_text(f"Input:\n<code>{' '.join(msg.command[1:])}</code>\n\nResult:\n<code>{escape(result)}</code>")
    except Exception as excp:
        msg.edit_text(str(excp))
