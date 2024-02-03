/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java2_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * *************************ENUNCIADO******************************************
 * Ejercicio_3: Realiza un programa que muestre los números pares comprendidos
 *              entre el 1 y el 200; esta vez utiliza un contador sumando 
 *              de 1 en 1.
 * ****************************************************************************
 */
public class Ejercicio_3 {
    public static void main(String[]args){
        
        //declaramos la variable que usaremos
        
        int num;
       
        /**
         * Declaramos un for en el que agregamos un condicional, para que solo 
         * nos muestre los números pares de la operación.
         */
       
        
        for ( num = 0; num < 201; num++) {
            if (num%2==0) {
                System.out.println(num);
            }
        }
    }
}
