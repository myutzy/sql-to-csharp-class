# SQL To C# Class
Need a quick way to generate a C# class from a SQL `CREATE` command? Use this simple Python script. It's much faster than typing the class by hand.

![image](https://user-images.githubusercontent.com/1199572/232250143-d1e6a49d-7273-40f7-9a18-ed9b399372cc.png)

## Features
- Interprets SQL column name, type, nullability and max length (if string) from input text
- Customizable output property template

## How do I use it?
- Modify `Input.txt` to contain only the column portion of your SQL `CREATE` command. Refer to the initial contents of `Input.txt` for an example.
- Run `python app.py`
- Results will be saved as `Output.cs`
