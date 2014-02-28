#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*cálculo pelo método de Simpson, regra 1/3*/

float M_simpson_h3(float M[2][30], int n)
{
	int c/*contador*/;
	int i;
	double delta , soma , douq/*variavel que decide se o f(x) sera multiplicado por 2 ou 4*/;
	delta = (fabs(M[0][1] - M[0][2]));
	soma = M[1][0];
	c = n-1;
	i = 1;
	douq = -1;
	while (i < c)
	{
		if (douq == -1)
		{
			soma = soma + 4 * M[1][i];
		}
		else
		{
			soma = soma + 2 * M[1][i];
		}
		i = i + 1;
		douq = douq * (-1);
	}
	soma = soma + M[1][i];
	return (soma * (delta / 3));
}

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

/*INÍCIO DO PROGRAMA*/

int main()
{
	float resultado = 0;
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

	resultado = M_simpson_h3(matriz, i);
	printf("Resultado: ");
	printf("%f   ", resultado);

	return EXIT_SUCCESS;
}
