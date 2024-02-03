/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java2_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * *************************ENUNCIADO******************************************
 * Ejercicio_4: Realiza un programa que muestre los números desde el 1 hasta 
 *              un número N que se introducirá por teclado.
 * ****************************************************************************
 */

//Importamos el java.util.scanner
import java.util.Scanner;
public class Ejercicio_4 {
    public static void main(String[]args){
    
        //Definimos la variable número que el scanner leerá
        
        int num;
        
        // Declaramos lector, el cual será un scanner
        
        Scanner lector = new Scanner(System.in);
        
        /**
         * Mostraremos en pantalla el mensaje que le indicará al usuario
         * las instrucciones.
         */
        
        System.out.println("Introduzca a continuación hasta qué número le "
                + "gustaría quue contara el bucle (Solo se permiten enteros).");
        
        //Agregamos un último indicador con un mensaje en la pantalla
        
        System.out.println("Intrrodúzcalo aquí: ");
        
        num = lector.nextInt();
        
        /**
         * Introducimos el bucle que nos dará la solución, y cno él el contador
         * i.
         */ 
    
        
         for ( int i = 0; i < (num+1); i++) {
            System.out.println(i);
        }
        
    }
}
