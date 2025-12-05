songs = [
    {
        'title': 'Lạc Trôi',
        'artist': 'Sơn Tùng MTP',
        'duration': 240
    },
    {
        'title': 'See Tình',
        'artist': 'Hoàng Thùy Linh',
        'duration': 180
    },
    {
        'title': 'Nơi Này Có Anh',
        'artist': 'Sơn Tùng MTP',
        'duration': 220
    }
]

print(songs)
def add_song():
    title = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    duration = int(input("Nhập thời lượng (giây): "))

    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }
    songs.append(song)
    print(">>> Đã thêm bài hát!")
def view_playlist():
    if len(songs) == 0:
        print("Playlist trống!")
    else:
        print("=== PLAYLIST ===")
        for i, s in enumerate(songs, 1):
            print(f"{i}. {s['title']} - {s['artist']} ({s['duration']}s)")
def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_song()
        elif choice == "2":
            view_playlist()     
        elif choice == "3":
            print(">>> Chức năng tìm theo ca sĩ (chưa làm).")
        elif choice == "4":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()