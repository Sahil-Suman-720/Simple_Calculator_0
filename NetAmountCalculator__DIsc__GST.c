#include<stdio.h>
#include<conio.h>
main()
{
    float salemt,discount,finalamt,netprice,gst;
    printf("enter sales amount: ");scanf("%f",&salemt);
    printf("\ndiscount percent: ");scanf("%f",&discount);
    discount = (discount*salemt)/100;
    finalamt = salemt - discount;
    printf("\nDiscount amount: %f \n", discount);
    printf("\nEnter gst: ");scanf("%f",&gst);
    gst = 0.18*finalamt;
    netprice = finalamt + gst;
    printf("\nNet price: $ %f",netprice);
    return 0;
}