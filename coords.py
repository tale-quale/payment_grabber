from pynput import mouse


def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")


if __name__ == "__main__":
    print("Click anywhere to see the coordinates. Press Ctrl+C to exit.")
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        print("\nExiting...")
        listener.stop()

# --- Original version (Ctrl+C may not work on some systems) ---
# if __name__ == "__main__":
#     print("Click anywhere to see the coordinates. Press Ctrl+C to exit.")
#     with mouse.Listener(on_click=on_click) as listener:
#         listener.join()