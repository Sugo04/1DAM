/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_02_Jedi;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*****************************************
 * Ejercicio_15: Escribe un programa que lea tres números distintos y 
 * nos diga cuál es el mayor.
 * ***************************************************************************
 */

//importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_15 {
    public static void main (String[] args){
        
        //Declaramos nuestras variables
        
        double num1, num2, num3;
        
        //Introducimos lector, entrada y puerto como scanners.
         Scanner lector = new Scanner(System.in);
        
        
        /**
         * Mostramos en pantalla un mensaje para indicar que deberán de hacer.
         */
        
        System.out.println("Ahora deberá de introducir tres números (pueden"
                + "tener decimales");
        
        /**
         * Indicaré con un mensaje donde deberá de introducir cada uno de los 
         * números requeridos para el ejercicio, así como introduciré los 
         * lectores.
         */
        
        System.out.println("Introduzca el primer número: ");
        
        num1 = lector.nextDouble();
        
        System.out.println("Introduzca el segundo número:  ");
        
        num2 = lector.nextDouble();
        
        System.out.println("Introduzca el tercer número");
        
        num3 = lector.nextDouble();
        
        /**
         * Ahora realizaremos los condicionantes necesarios, para comprobar cual 
         * de los tres números es mayor, y devolver con un mensaje
         * en la pantalla la solución.
         */
        
        if (num1>num2) 
        {
            if (num1>num3)
            {
                System.out.println(num1+" es el mayor");
            } 
            else 
            {
                System.out.println(num3+ " es el mayor");
            }
               
        } 
        else 
        {
            if (num2>num3) 
            {
                 System.out.println(num2+ " es el mayor");
            } 
            else 
            {
                 System.out.println(num3+ " es el mayor");
            }
        }
    }
}
