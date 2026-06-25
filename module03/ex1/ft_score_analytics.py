import sys


def main() -> None:
	scores: list[int] = []
	index: int = 1
	while index < len(sys.argv):
		try:
			score = int(sys.argv[index])
			scores.append(score)
		except ValueError:
			print(f"Invalid parameter: '{sys.argv[index]}'")
		index += 1
	if not scores:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
	else:
		print(f"Scores processed: {scores}")
		print(f"Total players: {len(scores)}")
		print(f"Total score: {sum(scores)}")
		print(f"Average score: {sum(scores) / len(scores)}")
		print(f"High score: {max(scores)}")
		print(f"Low score: {min(scores)}")
		print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
