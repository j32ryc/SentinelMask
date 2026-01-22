# SentinelMask 🛡️

> A lightweight, standalone privacy protection tool for Red Team operations and log analysis.

**SentinelMask** is designed to automate the sanitization of sensitive information (PII) from log files and text data. It ensures compliance and operational security by redaction before data exfiltration or sharing.

## 🚀 Features

* **Zero Dependency:** Compiled as a standalone Linux binary (ELF). No Python environment required on the target machine.
* **Regex-Powered Engine:** accurately detects and masks:
    * Mobile Phone Numbers (CN)
    * IPv4 Addresses
    * Email Addresses
    * ID Card Numbers
* **Detailed Reporting:** Provides execution statistics regarding masked entities.
* **Pipeline Friendly:** Supports command-line arguments for seamless integration into automated workflows.

## 🛠️ Installation & Usage

### Option 1: Using the Standalone Binary (Recommended for Targets)

Just drop the binary onto any Linux machine and run it.

```bash
# Make it executable
chmod +x dist/sentinel_v2

# Run sanitization
./dist/sentinel_v2 -i target.log -o cleaned.log
