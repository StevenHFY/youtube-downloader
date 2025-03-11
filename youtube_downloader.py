import os
import yt_dlp
from tqdm import tqdm

def format_size(bytes):
    """格式化文件大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} TB"

class ProgressHook:
    def __init__(self):
        self.pbar = None

    def __call__(self, d):
        if d['status'] == 'downloading':
            if self.pbar is None and 'total_bytes' in d:
                self.pbar = tqdm(
                    total=d['total_bytes'],
                    unit='B',
                    unit_scale=True,
                    desc='下载进度'
                )
            if self.pbar:
                if 'downloaded_bytes' in d:
                    self.pbar.update(d['downloaded_bytes'] - self.pbar.n)
                if d.get('finished', False):
                    self.pbar.close()

def list_formats(url):
    """列出可用的视频格式"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            print("\n可用的视频格式：")
            print("格式代码\t分辨率\t\t文件大小\t\t格式")
            print("-" * 70)
            
            for f in formats:
                format_id = f.get('format_id', 'N/A')
                ext = f.get('ext', 'N/A')
                resolution = f.get('resolution', 'N/A')
                filesize = format_size(f.get('filesize', 0)) if f.get('filesize') else 'N/A'
                format_note = f.get('format_note', '')
                
                print(f"{format_id}\t{resolution}\t{filesize}\t\t{ext} {format_note}")
            
            return True
    except Exception as e:
        print(f"\n获取格式信息失败: {str(e)}")
        return False

def download_video(url, output_path=None, format_id=None):
    """下载YouTube视频"""
    try:
        if output_path is None:
            output_path = os.path.join(os.getcwd(), "downloads")
        os.makedirs(output_path, exist_ok=True)

        progress_hook = ProgressHook()
        ydl_opts = {
            'format': format_id if format_id else 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
            'quiet': True,
            'no_warnings': True,
        }

        print("\n正在获取视频信息...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 获取视频信息
            info = ydl.extract_info(url, download=False)
            
            # 显示视频信息
            print("\n找到视频:")
            print(f"标题: {info.get('title', '未知')}")
            print(f"时长: {info.get('duration', 0)} 秒")
            print(f"视频质量: {info.get('resolution', '未知')}")
            if 'filesize' in info:
                print(f"预计文件大小: {format_size(info['filesize'])}")
            
            # 开始下载
            print("\n开始下载视频...")
            ydl.download([url])
            
            print(f"\n下载完成！视频保存在: {output_path}")
            return True

    except Exception as e:
        print(f"\n下载失败: {str(e)}")
        print("\n可能的原因：")
        print("1. 网络连接问题")
        print("2. 视频不存在或已被删除")
        print("3. 视频有地区限制")
        print("4. 需要登录才能访问")
        return False

def main():
    print("=== YouTube视频下载器 ===")
    print("提示：请确保您的视频链接格式如：https://www.youtube.com/watch?v=XXXXXXXXXXX")
    
    while True:
        url = input("\n请输入YouTube视频链接 (输入'q'退出): ").strip()
        if url.lower() == 'q':
            break
            
        if not url.startswith('http'):
            print("错误：请输入完整的视频链接，包含 'https://'")
            continue
        
        # 显示可用格式
        if not list_formats(url):
            continue
            
        format_id = input("\n请选择格式代码 (直接回车使用最佳质量): ").strip()
        if not format_id:
            format_id = None
            
        output_path = input("请输入保存路径 (直接回车使用默认路径): ").strip()
        if not output_path:
            output_path = None
            
        download_video(url, output_path, format_id)
        
    print("\n感谢使用！再见！")

if __name__ == "__main__":
    main() 