/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*********************************
 * Ejercicio_3: Escribe un programa que calcule el área de un cuadrado 
 *              cuyo lado se introduce por teclado.
 * *******************************************************************
 */
import java.util.Scanner;
public class Ejercicio_3 {
    
    public static void main(String[] args){
        
        double lado, área;
        
        //Declaro el objeto lector de la case Scanner
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Introduce la medida del lado del cuadrado");
        
        //Lo utilizaré para leer la variable lado desde el teclado
        lado = entrada.nextDouble();
        
        //El lado al cuadrado es el área
        área = Math.pow(lado, 2);
        
        //Muestro en pantalla el resultado
        System.out.println("El área del lado "+lado+" es: "+área);
        
        
    }
    
}
