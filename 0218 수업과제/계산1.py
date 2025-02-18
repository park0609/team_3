{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "559bdc65-593d-4500-87f9-358c6b27a714",
   "metadata": {},
   "outputs": [],
   "source": [
    "def birth():\n",
    "    import datetime\n",
    "    days = [\"월\",\"화\",\"수\",\"목\",\"금\",\"토\",\"일\"]\n",
    "    month = input(\"생일의 월을 입력해주세요!\")\n",
    "    day = input(\"생일의 일을 입력해주세요!\")\n",
    "    day1 = datetime.date(2025,2,18)\n",
    "    day2 = datetime.date(2025,int(month),int(day))\n",
    "    diff = day2 - day1\n",
    "    print(f\"생일까지 {diff.days}일 남았고, 그 날은 {days[day2.weekday()]}요일 입니다!\")\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbc1fd7d-cf55-4cdf-b6b5-79bee28c3ad9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b84e1774-ec1e-49e0-8bd2-9a246dddbd7b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
