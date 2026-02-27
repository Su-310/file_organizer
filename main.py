import argparse
import os
import shutil
import logging

logger = logging.getLogger("file_organizer")
logger.setLevel(logging.INFO)

# ===== 正常ログ (.log) =====
info_handler = logging.FileHandler(
    "file_organizer.log", encoding="utf-8"
)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
)

# ===== エラーログ (.err) =====
error_handler = logging.FileHandler(
    "file_organizer.err", encoding="utf-8"
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
)

logger.addHandler(info_handler)
logger.addHandler(error_handler)

def organize_files(target_dir, dry_run=False):
    try:
        for filename in os.listdir(target_dir):
            src = os.path.join(target_dir, filename)

            if os.path.isfile(src):
                ext = filename.split('.')[-1]
                dest_dir = os.path.join(target_dir, ext)
                os.makedirs(dest_dir, exist_ok=True)
                dest = os.path.join(dest_dir, filename)

                logger.info(f"Move: {src} -> {dest}")

                if not dry_run:
                    shutil.move(src, dest)

    except FileNotFoundError:
        logger.error(f"フォルダが見つかりません: {target_dir}")
    except PermissionError:
        logger.error("権限エラーが発生しました")
    except Exception:
        logger.exception("予期しない例外が発生しました")   
     
def main():
    parser = argparse.ArgumentParser(description="File organizer")
    parser.add_argument("target", help="整理対象フォルダ")
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    logger.info("=== Program start ===")
    logger.info(f"Arguments: target={args.target}, dry_run={args.dry_run}")

    organize_files(args.target, args.dry_run)

    logger.info("=== Program end ===")

if __name__ == "__main__":
    main()

