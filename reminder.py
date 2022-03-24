import os
import requests

OK_CODES = 200,201,203,203,204
root_url = "https://api.telegram.org/bot"
message = "Промониторьте, пожалуйста, чаты:\n https://t.me/VolunteerTalksLviv\n https://t.me/Lviv_help\n https://t.me/BelarusyVKieve\n https://t.me/bellviv\n ВОЛОНТЕРИ | ЛЬВІВ - тут ссылку не нашел, поищите по названию\n на предмет новых запросов по жилью или какой-то помощи и внесите на сайт"
target_group_chat_id = os.environ.get("target_group_chat_id")
bot_token = os.environ.get("bot_token")
chat_with_admin_id = os.environ.get("chat_with_admin_id")

def send_reminder():
	url = f"{root_url}{bot_token}/sendMessage"
	data = {"chat_id": target_group_chat_id,
			"text": message}
	res = requests.post(url, json=data)
	if res.status_code not in OK_CODES:
		fail_message = f"Message to group not delivered - failed with status_code {res.status_code}"
		data = {"chat_id": chat_with_admin_id,
				"text": fail_message}
		res = requests.post(url, json=data)

if __name__ == '__main__':
	try:
		send_reminder()
	except Exception as e:
		print(f"Reminder failed with error: {e}")
#sudo vim /etc/crontab