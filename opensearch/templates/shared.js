// 

// replace "document.querySelectorAll('.className');"
export const $$ = (tagName) => {
    // one or many params
    const elems = document.querySelectorAll(tagName);
    if (elems.length > 1) {
        return elems;
    } else if (elems.length ==1) {
        return elems[0];
    } // null if none found
}

export const preProcessCSV = function(inputText) {
    console.log("imported CSV DATA", inputText)
    let regex = /, /g   /// lastname, first name fields
    let cleantext = importedText.replace(regex, "_ ");
}

export const getConvertCSV = async (csvUrl) => {
    const response = await fetch(csvUrl); 
    const inputText = await response.text(); //convert csv into text

    let cleanedCSV = preProcessCSV(inputText)
    // convert text to json by splitting by line, the by comma
    const jsonRowObjectsString = await csvToJSON(cleanedCSV)
    console.log("jsonRowObjects String", jsonRowObjectsString)
    // TO JSON
    const jsonRowObjectsArray = JSON.parse(jsonRowObjectsString);
    // todo - write JSON to file.json in ./data/JSON/data9006_json.json
       return jsonRowObjectsArray;
}

export const csvToJSON = (csv) => {
    //split up text file into array of rows
    let rowsArray= csv.split("\n");
    
    let result = []; 
    let headers = rowsArray[0].split(",");
        // starts at 1, skipping header
    for(let i=1; i<rowsArray.length; i++) {
        let obj = new Object; //object mapper
        //divide each row into array
        let currentRow =  rowsArray[i].split(",");

        for (let j=0; j<headers.length; j++){
            // 2nd loop assigns cols to first header, then cols to 2nd header
            // arrs of headers are then mapped to their respective row "items"
            obj[headers[j]] = currentRow[j];   
        }
        result.push(obj);
    }
        //returns JSON array of row-objects
        return JSON.stringify(result);
}

export const csvTo2DArray = () => {
    const parseCSV = (data) => {
        const csvDataArray = [];
        const rows = data.split("\n");
        // loop through rows and return array of inidvidual strings within line separated by comma
        for (let i=0; i < rows.length; i++) {
            csvDataArray[i] = lines[i].split(",");
        }
        //returns array of row-arrays 2d array
        return csvDataArray;
        // [ [header1,header2,header3], [col1,col2,col3], [col1,col2,col3] ]
    }
}
