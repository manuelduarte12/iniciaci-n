#include<stdio.h>
#define SIZE 5

int value[SIZE], front = -1, rear = -1;



void enQueu(int value)
{
  if (rear == SIZE - 1)
    printf("Nuestro Queue esta lleno\n");
  else
  {
    if (front == -1)
      front = 0;
    rear++;
    items[rear] = value;
    printf("se inserto el valor coreecto %d\n");
  }
}

void deQueue(){
  if (front == -1)
    printf("Nuestro  Queue esta vacio\n");
  else
  {
    printf("Se elimino el valor %d", items[front]);
    front++;
    if(front > rear)
    front = rear = -1
  }
}

main(int argc, char const *argv[])
{
  deQueue();
  return 0;
}

