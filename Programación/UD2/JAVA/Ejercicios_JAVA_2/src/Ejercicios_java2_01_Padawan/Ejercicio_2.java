/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java2_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * *************************ENUNCIADO******************************************
 * Ejercicio_2: Realiza un programa que muestre los números pares comprendidos 
 *              entre el 1 y el 200; para ello utiliza un contador y suma 
 *              de 2 en 2.
 * ****************************************************************************
 */
public class Ejercicio_2 {
    
    public static void main(String[]args){
        
        //declaramos la variable que usaremos
        
        int num;
        
        //Declaramos el bucle, usamos for, que nos dará la solución.
        
        for ( num = 0; num < 201; num+=2) {
            System.out.println(num);
        }
    
    }
}
