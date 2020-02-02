import contextlib


def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False


def cleanup():
    print('clean up')


# finallyで後処理を実行したい
try:
    is_ok = is_ok_job()
    print('more task')
finally:
    if not is_ok:
        cleanup()


with contextlib.ExitStack() as stack:
    # 最後に行いたい後処理をcallbackに追加
    # 後処理があることを明示できて可読性が向上する
    stack.callback(cleanup)

    # デコレータでも可能
    # スタックなのでlast-in, first-outで後入れ先出し
    @stack.callback
    def cleanup2():
        print('clean up 2')

    is_ok = is_ok_job()

    # is_okなら後処理をpopする
    if is_ok:
        stack.pop_all()
