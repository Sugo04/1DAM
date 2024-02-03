/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_02_Jedi;

import java.util.Scanner;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*****************************************
 * Ejercicio_13: Escribe un programa que lee dos números y los visualiza 
 * en orden ascendente.
 * ***************************************************************************
 */
//Importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_13 {
     public static void main (String[] args){
        
        //Declaramos nuestras variables
        
        double num1, num2;
        
        //Introducimos lector y entrada como scanners.
         Scanner lector = new Scanner(System.in);
         
        
        /**
         * Mostramos en pantalla un mensaje para indicar que deberán de hacer.
         */
        
        System.out.println("Ahora deberá de introducir dos números (pueden"
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
        
        /**
         * Ahora realizaremos el condicionante necesario, para comprobar cual 
         * de sendos números es mayor, y devolver con un mensaje en la pantalla
         * la solución.
         */
        
        if (num1>num2) 
        {
            System.out.println("El orden ascendente de estos números es "+
                    num2+", "+num1);   
        } 
        else 
        {
            System.out.println("El orden ascendente de estos números es "+
                    num1+", "+num2);
        }
     }
}
