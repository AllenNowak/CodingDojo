/*
  Pokemon Finder

  This challenge will have 5 functions where, given an array, display the required information.
*/

var pokemon = [
    { id: 1, name: 'Bulbasaur', types: ['poison', 'grass'] },
    { id: 5, name: 'Charmeleon', types: ['fire'] },
    { id: 9, name: 'Blastoise', types: ['water'] },
    { id: 12, name: 'Butterfree', types: ['bug', 'flying'] },
    { id: 16, name: 'Pidgey', types: ['normal', 'flying'] },
    { id: 23, name: 'Ekans', types: ['poison'] },
    { id: 24, name: 'Arbok', types: ['poison'] },
    { id: 25, name: 'Pikachu', types: ['electric'] },
    { id: 37, name: 'Vulpix', types: ['fire'] },
    { id: 52, name: 'Meowth', types: ['normal'] },
    { id: 63, name: 'Abra', types: ['psychic'] },
    { id: 67, name: 'Machamp', types: ['fighting'] },
    { id: 72, name: 'Tentacool', types: ['water', 'poison'] },
    { id: 74, name: 'Geodude', types: ['rock', 'ground'] },
    { id: 87, name: 'Dewgong', types: ['water', 'ice'] },
    { id: 98, name: 'Krabby', types: ['water'] },
    { id: 115, name: 'Kangaskhan', types: ['normal'] },
    { id: 122, name: 'Mr. Mime', types: ['psychic'] },
    { id: 133, name: 'Eevee', types: ['normal'] },
    { id: 144, name: 'Articuno', types: ['ice', 'flying'] },
    { id: 145, name: 'Zapdos', types: ['electric', 'flying'] },
    { id: 146, name: 'Moltres', types: ['fire', 'flying'] },
    { id: 148, name: 'Dragonair', types: ['dragon'] },
  ];

  pokemon[0].types[0] // poison
  pokemon[0]['name'] // bulbasaur
  
  /**
   * console.log the pokemon objects whose id is evenly divisible by 3 
   * @param {Array<any>} pokemon
   * @returns {null} no return
   */
  function dividibleByThree(pokemon) {
    for(var poke of pokemon) {
        if( poke.id % 3 === 0) {
            console.log(poke)
        }
    }
  }
  dividibleByThree(pokemon)
  
  /**
   * console.log the pokemon objects that have more than one type
   * @param {Array<any>} pokemon
   * @returns {null} no return
   */
  function moreThanOneType(pokemon) {
    for(var poke of pokemon) {
        if( poke.types.length > 1) {
            console.log(poke)
        }
    }
  }
  moreThanOneType(pokemon)

  /**
   * console.log the names of the pokemon whose only type is 'poison'
   * @param {Array<any>} pokemon
   * @returns {null} no return
   */
  function poisonType(pokemon) {
    for(var poke of pokemon) {
        if( poke.types.length == 1 && poke.types == "poison") {
            console.log(poke.name)
        }
    }
  }
  poisonType(pokemon)

  /**
   * console.log the first type of all the pokemon whose second type is flying
   * @param {Array<any>} pokemon
   * @returns {null} no return
   */
  function flyingSecondType(pokemon) {
    for(var poke of pokemon) {
        if( poke.types.length > 1 && poke.types[1] == "flying") {
            console.log(poke.types[0])
        }
    }
  }
  flyingSecondType(pokemon)

  /**
   * console.log the reverse of the names of the pokemon whose only type is 'poison'
   * @param {Array<any>} pokemon
   * @returns {null} no return
   */
  function reversedNamesOfPoisonPokemon(pokemon) {
    for(var poke of pokemon) {
        if( poke.types.length === 1 && poke.types == "poison") {
          let reverse1 = poke.name.split('').reverse().join('');
          let reverse2 = poke.name.split('').reduceRight((prev, cur) => prev + cur);
          let reverse3 = ''
          for (let i = poke.name.length; i >= 0; i-- ) {
            reverse3 += poke.name[i]
          }
          
          console.log(reverse2)
        }
    }
  }

reversedNamesOfPoisonPokemon(pokemon)
  
