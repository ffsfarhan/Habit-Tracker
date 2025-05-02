# 🧠 Habit Tracker (Console-based)

This is a simple **Python mini project** that allows users to track their habits for a month. You can:
- Add new habits
- Mark them as completed for the day
- View your overall progress

---

## 📌 How It Works

1. **Add Habits**  
   The user is prompted to enter the number of habits they want to track and then input the names of those habits.

2. **Mark Completed Habits**  
   The user is then asked how many habits they have completed. They can enter the names of those completed habits, and the system will log them with the current date.

3. **View Progress (Optional)**  
   After logging, the user can choose to view a progress report which displays how many times each habit was completed and on which dates.

---

---

## 🛠️ Features

- Case-insensitive habit names.
- Tracks the date when a habit is marked as done.
- Displays total days a habit was done along with specific dates.

---

## 📂 Requirements

- Python 3.x
- No external libraries required

---

## 📎 Notes

- You can't mark more completed habits than you've added.
- Data is **not persistent** unless you enable JSON logging (see code comments).

---
## 🚀 Example Usage

Enter the number of habits for the month: 3

Enter Habit 1: Workout  
Enter Habit 2: Reading  
Enter Habit 3: Meditation

How many habits have you completed: 2

Enter Habit 1: Workout  
Enter Habit 2: Reading

Do you want to view your progress: yes

workout: Done on 1 day - ['2025-05-02']  
reading: Done on 1 day - ['2025-05-02']  
meditation: Not done yet


