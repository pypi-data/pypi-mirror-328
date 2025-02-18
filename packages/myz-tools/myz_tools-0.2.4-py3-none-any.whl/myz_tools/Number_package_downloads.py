import json
import subprocess
from datetime import datetime, timedelta


def get_monthly_downloads(package, start_date, end_date):
    """
    获取按月的下载量，区分镜像和官网

    :param package: 库名称 (str)
    :param start_date: 开始日期 (datetime.date)
    :param end_date: 结束日期 (datetime.date)
    :return: (monthly_downloads, total_with_mirrors, total_without_mirrors)
    """
    current_date = start_date
    monthly_downloads = {}
    total_with_mirrors = 0
    total_without_mirrors = 0

    while current_date < end_date:
        # 计算下个月的起始日期
        next_month = current_date.replace(day=28) + timedelta(days=4)
        next_month = next_month.replace(day=1)
        query_end_date = min(next_month, end_date)

        cmd = [
            "pypistats",
            "overall",
            package,
            "--start-date",
            current_date.isoformat(),
            "--end-date",
            query_end_date.isoformat(),
            "--json",
        ]
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, encoding="utf-8-sig", check=True
            )
        except subprocess.CalledProcessError:
            monthly_downloads[current_date.strftime("%Y-%m")] = {
                "with_mirrors": 0,
                "without_mirrors": 0,
                "total": 0,
            }
            current_date = next_month
            continue
        except Exception:
            monthly_downloads[current_date.strftime("%Y-%m")] = {
                "with_mirrors": 0,
                "without_mirrors": 0,
                "total": 0,
            }
            current_date = next_month
            continue

        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            monthly_downloads[current_date.strftime("%Y-%m")] = {
                "with_mirrors": 0,
                "without_mirrors": 0,
                "total": 0,
            }
            current_date = next_month
            continue

        downloads_with_mirrors = 0
        downloads_without_mirrors = 0

        if "data" in data:
            for entry in data["data"]:
                try:
                    if entry.get("category") == "with_mirrors":
                        downloads_with_mirrors = int(entry.get("downloads", 0))
                    elif entry.get("category") == "without_mirrors":
                        downloads_without_mirrors = int(entry.get("downloads", 0))
                except (ValueError, TypeError):
                    pass

        month_label = current_date.strftime("%Y-%m")
        monthly_downloads[month_label] = {
            "with_mirrors": downloads_with_mirrors,
            "without_mirrors": downloads_without_mirrors,
            "total": downloads_with_mirrors,  # 按原逻辑，总数取 with_mirrors 的值
        }
        total_with_mirrors += downloads_with_mirrors
        total_without_mirrors += downloads_without_mirrors

        current_date = next_month

    return monthly_downloads, total_with_mirrors, total_without_mirrors


def fetch_download_stats(
    package, start_date, end_date, output_path=None, show_monthly=True
):
    """
    主函数接口，供外部直接调用。传入库名称、起止日期，
    返回各月下载量及总数，同时支持：
      - 将结果输出到指定路径下的TXT文件（当 output_path 不为 None 时）
      - 根据 show_monthly 参数决定是否输出每个月详细结果

    :param package: 库名称 (str)
    :param start_date: 开始日期 (datetime.date)
    :param end_date: 结束日期 (datetime.date)
    :param output_path: 输出文件路径 (str) 可选，若为 None 则直接打印输出到控制台
    :param show_monthly: 是否输出每个月的详细结果 (bool)
    :return: (monthly_downloads, total_with_mirrors, total_without_mirrors)
    """
    (
        monthly_downloads,
        total_with_mirrors,
        total_without_mirrors,
    ) = get_monthly_downloads(package, start_date, end_date)

    output_lines = []
    if show_monthly:
        output_lines.append("Monthly Downloads Breakdown:")
        for month, data in monthly_downloads.items():
            output_lines.append(
                f"{month}: with_mirrors={data['with_mirrors']}, without_mirrors={data['without_mirrors']}, total={data['total']}"
            )
    output_lines.append("\nTotal Downloads:")
    output_lines.append(f"With mirrors: {total_with_mirrors}")
    output_lines.append(f"Without mirrors: {total_without_mirrors}")
    output_lines.append(f"Overall total: {total_with_mirrors}")
    output_str = "\n".join(output_lines)

    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output_str)
        except Exception as e:
            print(f"写入文件失败: {e}")
            print(output_str)
    else:
        print(output_str)

    return monthly_downloads, total_with_mirrors, total_without_mirrors


if __name__ == "__main__":
    package = "myz_tools"
    start_date = datetime(2024, 8, 1).date()
    end_date = datetime.now().date()
    # 若需输出详细每月数据，则 show_monthly 设置为 True；若只想输出总计，则设置为 False
    # fetch_download_stats(package, start_date, end_date, output_path="output.txt", show_monthly=True)
    fetch_download_stats(package, start_date, end_date, show_monthly=False)
