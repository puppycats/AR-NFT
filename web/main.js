var deviceWidth = window.screen.width;

fonts = ["'Andada Pro', serif", "'Anton', sans-serif", "'Archivo', sans-serif", "'BioRhyme', serif", "'Cormorant', serif", "'Encode Sans', sans-serif", "'Epilogue', sans-serif", "'Hahmlet', serif", "'Inter', sans-serif", "'JetBrains Mono', monospace", "'Lato', sans-serif", "'Lora', serif", "'Manrope', sans-serif", "'Montserrat', sans-serif", "'Nunito', sans-serif", "'Old Standard TT', serif", "'Open Sans', sans-serif", "'Oswald', sans-serif", "'Oxygen', sans-serif", "'Playfair Display', serif", "'Poppins', sans-serif", "'Raleway', sans-serif", "'Roboto', sans-serif", "'Sora', sans-serif", "'Source Sans Pro', sans-serif", "'Spectral', serif", "'Work Sans', sans-serif"]

const generate_header = () => {
    var img = Array(deviceWidth)
    var tmp = Array(100)
    for (var i = 0; i < deviceWidth; i++) {
        img[i] = tmp
        for (var j = 0; j < 100; j++) {
            b = Math.floor(Math.random() * 256);
            g = Math.floor(Math.random() * 256);
            r = Math.floor(Math.random() * 256);
            img[i][j] = [b, g, r]
        }
    }
    cv.imwrite("header.png", img);
    console.log("header.png generated");
}

const shuffle = (array) => {
    let i = array.length
    let j;

    while (i != 0) {
      j = Math.floor(Math.random() * i);
      i--;
      [array[i], array[j]] = [array[j], array[i]];
    }
  
    return array;
  }

const main_load = async () => {

    // change title coloure
    document.getElementsByClassName("title")[0].style.color = "rgb(255, 255, 255)";
    // change title font
    document.getElementsByClassName("title")[0].style.fontFamily = "Comic Sans MS";
    // generate array of 20 random colours (colour is an array of 3 numbers)
    var colours = Array(27)
    for (var i = 0; i < 27; i++) {
        colours[i] = Array(3)
        for (var j = 0; j < 3; j++) {
            colours[i][j] = Math.floor(Math.random() * 256);
        }
    }
    shuffle(fonts)
    for (var i = 0; i < 26; i++) {
        document.getElementsByClassName("title")[0].style.color = "rgb(" + colours[i][0] + ", " + colours[i][1] + ", " + colours[i][2] + ")";
        document.getElementsByClassName("title")[0].style.fontFamily = fonts[i];
        await new Promise(r => setTimeout(r, 100));
        console.log("font: " + fonts[i]);
    }

}


/*
font-family: 'Andada Pro', serif;
font-family: 'Anton', sans-serif;
font-family: 'Archivo', sans-serif;
font-family: 'BioRhyme', serif;
font-family: 'Cormorant', serif;
font-family: 'Encode Sans', sans-serif;
font-family: 'Epilogue', sans-serif;
font-family: 'Hahmlet', serif;
font-family: 'Inter', sans-serif;
font-family: 'JetBrains Mono', monospace;
font-family: 'Lato', sans-serif;
font-family: 'Lora', serif;
font-family: 'Manrope', sans-serif;
font-family: 'Montserrat', sans-serif;
font-family: 'Nunito', sans-serif;
font-family: 'Old Standard TT', serif;
font-family: 'Open Sans', sans-serif;
font-family: 'Oswald', sans-serif;
font-family: 'Oxygen', sans-serif;
font-family: 'Playfair Display', serif;
font-family: 'Poppins', sans-serif;
font-family: 'Raleway', sans-serif;
font-family: 'Roboto', sans-serif;
font-family: 'Sora', sans-serif;
font-family: 'Source Sans Pro', sans-serif;
font-family: 'Spectral', serif;
font-family: 'Work Sans', sans-serif;
*/