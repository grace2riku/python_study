import threading

# 共有リソース
counter = 0

# Lockオブジェクトの作成
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000000):
        # Lockの取得
        lock.acquire()  # ★Lock取得
        try: # ★
            counter += 1
        finally: # ★
            # Lockの解放
            lock.release() # ★Lock開放

# 2つのスレッドで関数を実行
t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)  # 期待値: 2000000
