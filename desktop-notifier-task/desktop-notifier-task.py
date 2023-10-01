from plyer import notification
import time

def desktop_notifier(title, message, timeout):
    notification.notify(
        title = title,
        message = message,
        app_name = 'Task Notifier',
        timeout = timeout,  # Added timeout parameter
    )

if __name__ == "__main__":
    task_title = "Complete Task"
    task_message = "Don't forget to complete the specific task!"
    notification_timeout = 10  # Set the notification timeout in seconds

    desktop_notifier(task_title, task_message, notification_timeout)
