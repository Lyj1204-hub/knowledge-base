from .services import NoteService
from .storage import NoteStorage


def print_notes(notes) -> None:
    if not notes:
        print("暂无笔记记录")
        return
    print("\n笔记列表：")
    for note in notes:
        print(f"[{note.id}] {note.title} | {note.category} | {note.status}")


def run_menu() -> None:
    service = NoteService(NoteStorage())
    while True:
        print("\n===== Knowledge Base =====")
        print("1. 新增笔记")
        print("2. 查看全部笔记")
        print("3. 按分类查看")
        print("4. 按状态查看")
        print("5. 修改学习状态")
        print("6. 删除笔记")
        print("0. 退出")
        choice = input("请选择：").strip()
        try:
            if choice == "1":
                note = service.add_note(
                    title=input("笔记标题：").strip(),
                    content=input("笔记内容：").strip(),
                    category=input("笔记分类：").strip(),
                    source_url=input("参考链接（可留空）：").strip(),
                    summary=input("个人总结（可留空）：").strip(),
                )
                print(f"新增成功，笔记编号是：{note.id}")
            elif choice == "2":
                print_notes(service.list_notes())
            elif choice == "3":
                print_notes(service.list_notes(category=input("分类：").strip()))
            elif choice == "4":
                print_notes(service.list_notes(status=input("学习状态：").strip()))
            elif choice == "5":
                note_id = int(input("笔记编号："))
                status = input("新学习状态：").strip()
                note = service.update_status(note_id, status)
                print("学习状态修改成功" if note else "没有找到这个笔记")
            elif choice == "6":
                note_id = int(input("笔记编号："))
                print("删除成功" if service.delete_note(note_id) else "没有找到这个笔记")
            elif choice == "0":
                print("程序已退出")
                break
            else:
                print("请输入 0 到 6 之间的数字")
        except ValueError as exc:
            print(f"操作失败：{exc}")


if __name__ == "__main__":
    run_menu()
