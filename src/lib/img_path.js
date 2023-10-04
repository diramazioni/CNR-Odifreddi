/**
 * returns an array of image paths
 * @param {string} dir
 * @returns {string[]}
 */
export function getImgPath(dir) {
  let imageModules={};
  let imagePath = [];
  switch (dir) {
    case "1-1": 
      imageModules = import.meta.glob("$lib/assets/1-1/*.jpg"); 
    case "1-2": 
      imageModules = import.meta.glob("$lib/assets/1-2/*.jpg"); 
    case "1-3": 
      imageModules = import.meta.glob("$lib/assets/1-3/*.jpg"); 
    case "1-4": 
      imageModules = import.meta.glob("$lib/assets/1-4/*.jpg"); 
  }
  imagePath = Object.keys(imageModules).map((key) => imageModules[key].name);
  console.log(imagePath)
  return imagePath
}