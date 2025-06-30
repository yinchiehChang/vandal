#!/usr/bin/env python3
import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


# ====== 配置区 ======
SRC_DIR = os.path.join("dataset", "hex")  # 输入目录
DST_DIR = "outputs_tac"                   # 输出目录
DECOMPILE_CMD = [sys.executable, os.path.join("bin", "decompile")]
MAX_WORKERS = 4  # 并发线程数，可根据机器性能调整
# =====================

def decompile_one(fname):
    base = os.path.splitext(fname)[0]
    in_path  = os.path.join(SRC_DIR, fname)
    out_path = os.path.join(DST_DIR, base + ".tac")

    # 已经存在就跳过
    if os.path.isfile(out_path):
        return fname + " (skipped)"

    # 否则执行 decompile
    cmd = DECOMPILE_CMD + [in_path, out_path]
    subprocess.run(cmd, check=True)
    return fname

def main():
    # 确保输出目录存在
    os.makedirs(DST_DIR, exist_ok=True)

    # 收集所有 .hex 文件
    all_hex = [f for f in os.listdir(SRC_DIR) if f.lower().endswith(".hex")]

    # 创建线程池 + 进度条
    pbar = tqdm(total=len(all_hex), desc="Decompiling", unit="file")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exe:
        futures = {exe.submit(decompile_one, f): f for f in all_hex}
        for fut in as_completed(futures):
            try:
                result = fut.result()
                # 更新右侧的当前文件名
                pbar.set_postfix_str(result)
            except Exception as e:
                pbar.set_postfix_str(f"ERROR: {futures[fut]}")
                # 如果需要，你也可以打印错误
                print(f"[ERROR] {futures[fut]}: {e}", file=sys.stderr)
            finally:
                pbar.update(1)

    pbar.close()

if __name__ == "__main__":
    main()
