import os
import subprocess

# 方式1：使用subprocess
log_dir = "runs/"
port = 6006

process = subprocess.Popen([
    'tensorboard',
    '--logdir', log_dir,
    '--port', str(port),
    '--host', '0.0.0.0'
])

print(f"TensorBoard started at http://localhost:{port}")
print(f"Press Ctrl+C to stop")

# 保持运行
try:
    process.wait()
except KeyboardInterrupt:
    process.terminate()
