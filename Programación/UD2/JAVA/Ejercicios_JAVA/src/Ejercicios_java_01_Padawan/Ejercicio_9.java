/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*****************************************
 * Ejercicio_9: Escribe un programa que pide la edad por teclado y nos muestra 
 * el mensaje de “eres mayor de edad” o el mensaje de “eres menor de edad”.
 * ***************************************************************************
 */

//Voy a tomar casi el código completo del ejercicio 8.

import java.util.Scanner;
public class Ejercicio_9 {
    
    public static void main(String[] args){
        
        //Definimos las variables que vamos a usar
        int edad;
        
        //Declaro el objeto lector el cual es un scanner
        Scanner  lector= new Scanner(System.in);
    
        /**
         * Ahora muestro en pantalla el mensaje que dirá que se introduzca el 
         * valor para la edad.
         */
        
        System.out.println("Introduzca su edad: ");
        
        //Introducimos el aparatado de entrada de la distancia en millas
        edad = lector.nextInt();
        
        /**
         * introduciré las condiciones para resolver el ejercicio, y pondré 
         * lo que debe de hacer en caso de que no se cumpla la condición.
         */
        
        if (edad>=18)
        {
            //Muestro en pantalla el mensaje correspondiente a la solución.
            System.out.println("Eres mayor de edad.");
        }
        else 
        {
            //Muestro en pantalla el mensaje correspondiente a la solución.
            System.out.println("Eres menor de edad");
        }
    }
}