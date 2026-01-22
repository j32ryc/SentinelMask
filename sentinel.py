import re
import sys

# 红队自动化工具：敏感数据清洗引擎 (SentinelMask Lite)
def mask_data(text):
    print(f"[*] Analyzing content length: {len(text)} chars...")
    
    # 1. 猎杀手机号 (匹配 138-xxxx-xxxx 或纯数字)
    text = re.sub(r'(1[3-9]\d{9})', r'[PHONE_MASKED]', text)
    
    # 2. 猎杀 IP 地址 (匹配 IPv4)
    text = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', r'[IP_MASKED]', text)
    
    # 3. 猎杀邮箱
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', r'[EMAIL_MASKED]', text)
    
    return text

if __name__ == "__main__":
    print("\n>>> SentinelMask Security Engine Initialized <<<\n")
    
    # 模拟一条包含敏感信息的黑客日志
    raw_log = "ALERT: User admin (13988886666) login from 192.168.50.1 via email root@darkweb.com"
    
    print(f"[-] Raw Log:    {raw_log}")
    print("-" * 60)
    
    # 执行清洗
    clean_log = mask_data(raw_log)
    
    print(f"[+] Clean Log:  {clean_log}")
    print("\n>>> Process Completed. Data is now safe to export. <<<")
