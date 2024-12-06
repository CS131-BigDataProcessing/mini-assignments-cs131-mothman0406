#!/usr/bin/env nextflow

// Import the parameter from the config file
params.input_string = "Hello World"

// Define a process to convert the string to uppercase
process convertToUppercase {
    input:
    val string_input from params.input_string

    output:
    val uppercase_string into result_channel

    script:
    """
    echo \$string_input | tr '[:lower:]' '[:upper:]'
    """
}

// Run the process and capture the output
workflow {
    convertToUppercase()
    result_channel.view { println "Uppercase: $it" }
}

