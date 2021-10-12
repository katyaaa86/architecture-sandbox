# Architecture sandbox

Welcome to the architecture sandbox. 
It helps you to get acquainted with the basics of building abstractions in practice.

# Tasks

1. ### Abstraction design

You have some code in `abstraction` module, that calculate distance between two points on the surface of the earth.
This code uses [haversine formula](https://congyuzhou.medium.com/%D1%80%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5-%D0%BC%D0%B5%D0%B6%D0%B4%D1%83-%D0%B4%D0%B2%D1%83%D0%BC%D1%8F-%D1%82%D0%BE%D1%87%D0%BA%D0%B0%D0%BC%D0%B8-%D0%BD%D0%B0-%D0%BF%D0%BE%D0%B2%D0%B5%D1%80%D1%85%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B7%D0%B5%D0%BC%D0%BB%D0%B8-a398352bfbde).

**To do:** Explore the reading list below and rewrite `abstraction` module
with needed interface using theory of abstractions.

**To read:**
1. [Data abstraction](https://wizardforcel.gitbooks.io/sicp-in-python/content/9.html)
2. [Abstraction and composition](https://devpractice.ru/fp-python-part3-abs-comp-data-1/)
3. [What are leaky abstractions?](https://medium.com/young-coder/what-are-leaky-abstractions-an-illustrated-guide-f2982ff21cae)
4. [The Law of Leaky Abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

---
2. ### Design patterns
    
You have some code in `design_patterns` module. 

**To do:** Add code in every file of this module using design patterns.
You must choose the needed pattern in each case on your own.

**To read:**
1. [Refactoring guru](https://refactoring.guru/ru/design-patterns/python)
2. [Creational patters](https://docs.google.com/presentation/d/16C4gKm4XI9wltJbcBISfkhxKWS8Mk3BD/edit?usp=sharing&ouid=108787278912640858331&rtpof=true&sd=true)
3. [Structural and behavior patterns](https://docs.google.com/presentation/d/1knAh1qHFtn6E6UB-RurbOWZbSpr36mLo/edit?usp=sharing&ouid=108787278912640858331&rtpof=true&sd=true)


**Exercises:**
1. #### Message sender

Let’s say you want to build your own marketing software. You begin by writing some 
code to send messages with `smtplib`.  
You implement a message sender as a class, since you suspect that if you are going to build
larger systems you will need to work in an object-oriented way.  
```python
class Sender:
    def send(self, sender: str, recipient: str, message: str) -> None:
        msg = MIMEText(message)
        msg['From'] = sender
        msg['To'] = recipient

        mail_sender = smtplib.SMTP('localhost')
        mail_sender.send_message(msg)
        mail_sender.quit()
```
In another part of your project you use `Logger` class to log any events in console with `output`.  
```python
class Logger:
    def output(self, message: str) -> None:
        print(message)
```
User interface in your project contains only `send` method to send messages. 
```python
if __name__ == '__main__':
    sender = Sender()
    sender.send(
        'me@example.com',
        'another@example.com',
        'This is your message',
    )
```
- Add some code to `message_sender.py` to log all info when send message in console.
- Add ability to send messages to WhatsApp using [twilio](https://www.twilio.com/blog/send-whatsapp-message-30-seconds-python).  
!!Do not change user interface

2. #### Files parser

Imagine, that your company works with files and you need to proccess files with different extensions every day.  
The most popular functions, that you use: parsing files content to dict, to string and adding new information to files.  

- Create `parse_file.py`, where you can process csv and xlsx files, using common interface (choose right pattern)
- Write methods for every type of file: `parse_rows_to_dict()`, `add_row(new_raw: dict)`, `parse_rows_to_list`.
- Use `users.csv` and `users.xlsx` to test your code
- `sheet2dict` and `openpyxl` from requirements will help you in files processing
