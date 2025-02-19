import os
import json
import getpass
import argparse
import subprocess

CONFIG_FILE = os.path.expanduser('~/.glory_config')

def load_config():
    """加载配置文件"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    """保存配置到文件"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def add_new_server():
    """添加新的服务器配置"""
    config = load_config()
    
    print("请输入服务器信息：")
    label = input("标签名称: ").strip()
    hostname = input("主机地址: ").strip()
    username = input("用户名: ").strip()
    
    config[label] = {
        'hostname': hostname,
        'username': username
    }
    
    save_config(config)
    print(f"\n服务器 {label} 配置已保存")

def connect_server(label):
    """连接到指定的服务器"""
    config = load_config()
    if label not in config:
        print(f"未找到标签为 {label} 的服务器配置")
        return
    
    server = config[label]
    ssh_command = f"ssh {server['username']}@{server['hostname']}"
    
    try:
        subprocess.run(ssh_command, shell=True)
    except KeyboardInterrupt:
        print("\n已断开连接")

def list_servers():
    """列出所有保存的服务器配置"""
    config = load_config()
    if not config:
        print("没有保存的服务器配置")
        return
    
    print("\n当前保存的服务器列表：")
    print("-" * 50)
    print(f"{'标签名':<15}{'用户名':<15}{'主机地址':<20}")
    print("-" * 50)
    for label, info in config.items():
        print(f"{label:<15}{info['username']:<15}{info['hostname']:<20}")
    print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description='Glory SSH 远程管理工具')
    parser.add_argument('-n', '--new', action='store_true', help='添加新的服务器配置')
    parser.add_argument('-c', '--connect', metavar='LABEL', help='通过标签连接服务器')
    parser.add_argument('-l', '--list', action='store_true', help='列出所有保存的服务器')
    
    args = parser.parse_args()
    
    if args.new:
        add_new_server()
    elif args.connect:
        connect_server(args.connect)
    elif args.list:
        list_servers()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
