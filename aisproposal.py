from textwrap import fill


WIDTH = 72
BLUE = "\033[94m"
GOLD = "\033[93m"
RESET = "\033[0m"

reasons = [
	("It ensures that I learn appropriately", "It is widely known that teachers in some public schools do not always attend their classes when it is time to teach. This can leave students to decide whether or not to learn. In addition, the peer pressure some students face can lead to harmful choices, including drug use, which may affect their concentration and character negatively."),
	("There is more order", "In some public schools, students are known to mistreat their peers without facing serious consequences. However, schools like AIS maintain discipline and order. I have personally heard of instances where offenders were removed from the boarding house or even expelled from the school."),
	("It prevents stress for my parents", "Going to AIS instead of Opoku Ware School would save my parents the stress of taking each child to a different school. They would only need to travel to one destination. Also, having siblings in the same school would allow us to look out for one another and strengthen our bond."),
	("Akosombo International School is highly ranked", "According to WAEC, Akosombo International School is ranked among the top private high schools in Ghana. More information can be found here: https://www.pulse.com.gh/story/top-5-private-high-schools-in-ghana-according-to-waec-2024072314484083488"),
]


def line(char="═"):
	return char * WIDTH


def print_proposal():
	print(f"{BLUE}{line()}\n{'A FORMAL PROPOSAL'.center(WIDTH)}\n{line()}{RESET}")
	print(f"{GOLD}{'Reasons Why I Should Go to AIS Instead of OWASS'.center(WIDTH)}{RESET}\n")

	for number, (heading, body) in enumerate(reasons, 1):
		print(f"{BLUE}{number}. {heading}{RESET}")
		print(fill(body, WIDTH - 4, initial_indent="   ", subsequent_indent="   "))
		print()

	conclusion = ("These are four reasons why I believe I should go to AIS instead of OWASS. "
				  "I promise that, if given the opportunity, I will work hard to make you proud. "
				  "I will strive to place among the top five consistently and work toward earning "
				  "a prefectorial position at AIS.")
	print(fill(conclusion, WIDTH))
	print("\nI hope you will allow me to attend AIS.\n")
	print("Yours truly,\nKirk")
	print(f"\n{BLUE}{line('─')}{RESET}")


if __name__ == "__main__":
	print_proposal()
