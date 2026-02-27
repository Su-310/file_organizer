import argparse
import os
import shutil
import logging

def organize_files(target_dir, dry_run=False):
    try:
        for filename in os.listdir(target_dir):
            src = os.path.join(target_dir, filename)

            if os.path.isfile(src):
                ext = filename.split('.')[-1]
                dest_dir = os.path.join(target_dir, ext)

                os.makedirs(dest_dir, exist_ok=True)
                dest = os.path.join(dest_dir, filename)

                logging.info(f"Move: {src} -> {dest}")

                if not dry_run:
                    shutil.move(src, dest)

    except FileNotFoundError:
        logging.error(f"フォルダが見つかりません: {target_dir}")
    except PermissionError:
        logging.error("権限エラーが発生しました")
    except Exception as e:
        logging.exception(f"予期しないエラー: {e}")
        
def main():
    parser = argparse.ArgumentParser(description="File organizer")
    parser.add_argument("target", help="整理対象のフォルダ")
    parser.add_argument("--dry-run", action="store_true", help="実際には移動しない")

    args = parser.parse_args()
    organize_files(args.target, args.dry_run)

if __name__ == "__main__":
    main()

