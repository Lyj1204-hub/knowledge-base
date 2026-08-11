from .services import JobService
from .storage import JobStorage


def hello():
    return "Hello, Job Assistant!"


def print_jobs(jobs):
    if not jobs:
        print("暂无岗位记录")
        return

    for job in jobs:
        print(
            f"[{job.id}] "
            f"{job.company} | "
            f"{job.title} | "
            f"{job.city} | "
            f"{job.status}"
        )


def main():
    service = JobService(JobStorage())

    while True:
        print("\n===== Job Assistant =====")
        print("1. 新增岗位")
        print("2. 查看全部岗位")
        print("3. 按状态查看")
        print("4. 修改投递状态")
        print("5. 删除岗位")
        print("0. 退出")

        choice = input("请选择：").strip()

        try:
            if choice == "1":
                company = input("公司名称：")
                title = input("岗位名称：")
                city = input("城市：")
                url = input("岗位链接：")
                note = input("备注：")

                job = service.add_job(
                    company=company,
                    title=title,
                    city=city,
                    url=url,
                    status="待投递",
                    note=note,
                )

                print(f"新增成功，岗位编号为 {job.id}")

            elif choice == "2":
                print_jobs(service.list_jobs())

            elif choice == "3":
                status = input("请输入状态：")
                print_jobs(service.list_jobs(status))

            elif choice == "4":
                job_id = int(input("岗位编号："))
                status = input("新状态：")

                service.update_status(job_id, status)
                print("状态修改成功")

            elif choice == "5":
                job_id = int(input("岗位编号："))

                service.delete_job(job_id)
                print("删除成功")

            elif choice == "0":
                print("程序退出")
                break

            else:
                print("无效选项")

        except ValueError as error:
            print(f"操作失败：{error}")


if __name__ == "__main__":
    main()