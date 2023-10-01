from plyer import notification
import time

def desktop_notifier(title, message):
    notification.notify(
        title = title,
        message = message,
        app_name = 'Task Notifier',  # Set a custom app name
        timeout = 10,  # Notification timeout in seconds
    )

if __name__ == "__main__":
    task_title = "Complete Task"
    task_message = "Don't forget to complete the specific task!"

    desktop_notifier(task_title, task_message)
