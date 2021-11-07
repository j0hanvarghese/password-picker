{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "acf924c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the random password is:\n",
      "standingshark55?\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "adj=['running','walking','talking','reading','standing']\n",
    "noun=['cat','horse','baby','monkey','shark']\n",
    "num=list(range(0,100))\n",
    "char=['?','@','$','%','&']\n",
    "sample_adj=random.choice(adj)\n",
    "sample_noun=random.choice(noun)\n",
    "sample_num=random.choice(num)\n",
    "sample_char=random.choice(char)\n",
    "password=str(sample_adj)+str(sample_noun)+str(sample_num)+str(sample_char)\n",
    "print('the random password is:')\n",
    "print(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4db44746",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d622ce5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
