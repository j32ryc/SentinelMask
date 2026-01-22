#!/usr/bin/env python3
import re
import argparse
import sys
import os
import time

class SentinelMask:
    def __init__(self):
        # 扩展的敏感特征库
        self.patterns = {
            'PHONE': r'(?<!\d)(?:(?:\+?86)|(?:86))?(1[3-9]\d{9})(?!\d)', # 优化手机号匹配
            'IPV4': r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
            'EMAIL': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            'ID_CARD': r'\b\d{15,18}[0-9Xx]?\b'
        }

    def mask_content(self, text):
        """核心脱敏引擎"""
        masked_text = text
        stats = {key: 0 for key in self.patterns}

        for label, pattern in self.patterns.items():
            # 查找并统计
            matches = re.findall(pattern, masked_text)
            stats[label] += len(matches)
            
            # 替换为 [LABEL_MASKED]
            replacement = f"[{label}_MASKED]"
            masked_text = re.sub(pattern, replacement, masked_text)
        
        return masked_text, stats

    def run(self, input_file, output_file):
        start_time = time.time()
        
        if not os.path.exists(input_file):
            print(f"[-] Error: Target file '{input_file}' not found.")
            sys.exit(1)

        print(f"[*] Target locked: {input_file}")
        print(f"[*] Reading data stream...")
        
        try:
            with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            original_size = len(content)
            print(f"[*] Processing {original_size} bytes of data...")
            
            # 执行清洗
            safe_content, stats = self.mask_content(content)
            
            # 写入结果
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(safe_content)

            # 输出战报
            elapsed = time.time() - start_time
            print("\n" + "="*40)
            print(f" >> MISSION COMPLETE ({elapsed:.2f}s) <<")
            print("="*40)
            for key, count in stats.items():
                if count > 0:
                    print(f" [+] Masked {key}:\t{count} instance(s)")
            print(f"\n[*] Clean data saved to: {output_file}")

        except Exception as e:
            print(f"[-] Critical Failure: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SentinelMask V2.0 - Red Team Privacy Tool")
    parser.add_argument("-i", "--input", required=True, help="Input log file path")
    parser.add_argument("-o", "--output", default="clean.log", help="Output file path")
    args = parser.parse_args()

    bot = SentinelMask()
    bot.run(args.input, args.output)
