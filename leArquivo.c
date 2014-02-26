#include <stdio.h>
#include <stdlib.h>

void leArquivo(float matriz[2][30], int *i)
{
    FILE *f;
    float x, y;
    int z;
    z = 0;
    f = fopen("input.txt","r");
    if(f == NULL)
    {
        printf("ERRO ao abrir arquivo.\n");;
    }else
    {
        fscanf(f,"%d",i);
        while(!feof(f))
        {
            fscanf(f,"%f %f",&x,&y);
            matriz[0][z] = x;
            matriz[1][z] = y;
            z++;
        }
    }

}

int main()
{
    float matriz[2][30];
    int i = 0;
    leArquivo(matriz, &i);
    int x,y;
    for(x = 0; x<i; x++){
        for(y = 0; y<2; y++)
            {
                printf("%f  ", matriz[y][x]);
            }
        printf("\n");
    }
}
