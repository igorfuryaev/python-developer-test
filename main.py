import json
from datetime import datetime


class Member:
    def __init__(self, number, name, surname, result_time, place=1):
        self.Name = name
        self.Surname = surname
        self.ResultTime = result_time
        self.Number = number
        self.Place = place

    def as_dict(self):
        return {
            'Нагрудный номер': self.Number,
            'Имя': self.Name,
            'Фамилия': self.Surname,
            'Результат': str(self.ResultTime)
        }


def sort_by_time(self):
    return self.ResultTime


with open('results_RUN.txt', encoding='utf-8-sig') as file:
    lines = file.readlines()

with open("competitors2.json", "r", encoding='utf-8-sig') as file:
    input_data = json.load(file)

member_counter = 0
person_objects = []

for input_string in lines:
    split_string = input_string.split()
    if split_string[1] == "start":
        time_str = split_string[2]
        time_object = datetime.strptime(time_str, '%H:%M:%S,%f')
        finish_line = lines[member_counter + 1]
        split_string_finish = finish_line.split()
        time_str_finish = split_string_finish[2]
        time_object_finish = datetime.strptime(time_str_finish, '%H:%M:%S,%f')
        result = time_object_finish - time_object
        person_objects.append(
            Member(split_string[0], input_data[split_string[0]]["Name"],
                   input_data[split_string[0]]["Surname"], result))

    member_counter = member_counter + 1
person_objects.sort(key=sort_by_time)

print("Результат", "\n")
print("| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |")
print("| --- | --- | --- | --- | --- |")

place_counter = 1

output_data = {}
for output_person_objects in person_objects:
    print("| ", place_counter, "| ", output_person_objects.Number, "| ", output_person_objects.Name, "| ",
          output_person_objects.Surname, "| ", output_person_objects.ResultTime, "|")
    output_person_objects.Place = place_counter
    place_counter = place_counter + 1
    output_data[output_person_objects.Place] = output_person_objects.as_dict()

with open("final_results.json", "w") as write_file:
    json.dump(output_data, write_file, ensure_ascii=False)
