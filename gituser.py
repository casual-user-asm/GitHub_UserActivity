import argparse
import requests


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('username', type=str, help="User info about you want to know")
	args = parser.parse_args()
	user_data = requests.get(f'https://api.github.com/users/{args.username}/events')
	parsed_data = user_data.json()
	repo_names = {}

	if len(parsed_data) == 0:
		print('Invalid username or API troubles, if username is correct, that mean we have some trouble with API')
		return 0

	for event in parsed_data:
		if event['type'] == "PushEvent":
			if event['repo']['name'] in repo_names:
				repo_names[event['repo']['name']] += 1
			else:
				repo_names[event['repo']['name']] = 1

	for k,v in repo_names.items():
		print(f'{args.username} make {v} commits to {k} repository')


if __name__=="__main__":
	main()
