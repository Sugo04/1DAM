/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_03_Maestro_jedi;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*****************************************
 * Ejercicio_16: Escribe un programa que lea una calificación numérica
 * entre 0 y 10 y la transforma en calificación alfabética,escribiendo el 
 * resultado.
 * ***************************************************************************
 */
//Importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_16 {
    
     public static void main (String[] args){
        
        //Declaramos nuestras variables
        
        double nota;
        
        //Introducimos lector y entrada como scanners.
         Scanner lector = new Scanner(System.in);
         
        
        /**
         * Mostramos en pantalla un mensaje para indicar que deberán de hacer.
         */
        
        System.out.println("Ahora deberá de introducir la nota "
                + "correspondiente (puede tener decimales)");
        
        /**
         * Indicaré con un mensaje donde deberá de introducir el número del que
         * se desea conocer su signo.
         */
        
        System.out.println("Introduzca  número: ");
        
        nota = lector.nextDouble();
        
        /**
         * Ahora realizaremos un encadenamiento de ifelse debido a que estamos 
         * usando números decimales, los cuales el switch no es capaz de leer;
         * E iremos mostrando las soluciones en la pantallas.
         * 
         */
        
         if (nota<3) {
             System.out.println("Muy insuficiente");
             
         } else {
             if (nota<5) {
                 System.out.println("Insuficiente");
             } else {
                 if (nota<6) {
                     System.out.println("Suficiente");
                 } else {
                     if (nota<9) {
                         System.out.println("Notable");
                         
                     } else {
                         if (nota<=10) {
                             System.out.println("Sobresaliente");
   
                         }
                     }
                 }
             }

         }
        
         
     }
}
