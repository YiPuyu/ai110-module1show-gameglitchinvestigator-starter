# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---1. When the game renew, it still shows game over and no more chance to submit guess 2.when mode is easy, it still shows the number bigger than 20 3. it just shows the guess number needs to be higher, but actually the number need to be smaller

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Root cause of the bug: The new_game function reset the attempts and secret values in the session state, but it failed to reset the status variable.

How I fixed it: I added the line st.session_state.status = "playing" to bring the game state back to normal.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Initial problem: The game would only say "Too high" for every guess I made.

AI suggestion: The AI recommended removing the odd/even validation logic and passing the integer value of secret directly.

What I found after applying it: When I ran the game again, the logic for the "lower" and "higher" hints was still reversed.

How I fixed it: I then opened logic_utils.py and manually corrected the comparison logic (e.g., swapping > and <).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when the game's behavior matched what I expected. For example, after fixing the hint logic, I tested guessing a number lower than the secret and confirmed it said "Too low" instead of "Too high". I also made sure the fix worked consistently across multiple rounds of the game.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a manual test by playing the game several times with different inputs. One test was guessing 30 when the secret was 50, which previously gave the wrong hint but now correctly showed "Too low". This confirmed that the comparison logic in logic_utils.py was finally correct.
- Did AI help you design or understand any tests? How?
Yes, AI helped me write a pytest case to verify the hint logic automatically. I asked Copilot to generate a test that checks if the function returns "Too low" when the guess is below the secret. The AI's suggestion gave me a clear template, which I then adapted to cover both "too high" and "too low" cases.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns your entire script from top to bottom every time you interact with the app (like clicking a button or typing a guess). If you don't use st.session_state to store important values like the secret number or game status, they get reset on every rerun. I learned that you have to explicitly update session state variables to keep the game behavior consistent.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to reuse the habit of writing small, focused test cases (using pytest) before I manually play the game to check if a bug is fixed. It saved me time because I could verify the logic without having to click through the whole game every time. I also learned to ask AI to generate these tests, which made it even faster.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would first spend a few minutes understanding the structure of the code (which file does what) before asking AI for help. I noticed that when I asked vague questions, AI gave vague answers, but when I pointed to specific lines with #file:app.py or a #FIXME comment, the suggestions were much more useful.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I used to think AI would just give me perfect code, but now I see it as a collaborator that needs checking and testing. The real value isn't the code AI writes for you, but how it helps you think through problems faster.