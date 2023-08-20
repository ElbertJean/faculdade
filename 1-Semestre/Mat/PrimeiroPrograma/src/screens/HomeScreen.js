import React, {useState} from 'react'
import {StyleSheet, Text, View, TextInput, TouchableOpacity, Image} from 'react-native';
import rock from '../asset/rock.png';
import sadness from '../asset/sadness.png';
import happy from '../asset/happy.png';
import { useNavigation } from '@react-navigation/native';


const HomeScreen = () => {

    const navigation = useNavigation();

    const [idade, setIdade] = useState('');
    const [convite, setConvite] = useState('')
    const [verificacao, setVerificacao] = useState('')

    function Verificar() {
        if (idade >= 18 && convite == 1) {
            setVerificacao(1)
        } else {
            setVerificacao(0)
        }
    }

    return (
        <>
            <View style={style.container}>
                <View style={style.containerHeader}>
                    <Text style={style.titleHeader}>Bem vindo ao Rock in Rio</Text>
                    <TouchableOpacity onPress={() => navigation.navigate('Fest')} >
                        <Image source={rock} style={style.imageRockInRio}/> 
                    </TouchableOpacity>
                </View>
                <Text style={style.description}>Neste evento, você só pode entrar se:</Text>
                <Text style={style.subDescription}>For maior de 18 anos <Text style={style.and}>E</Text> tiver um convite</Text>
                <View style={style.containerInput}>
                    <Text style={style.label}>Qual a sua idade?</Text>
                    <TextInput
                        style={style.input}
                        onChangeText={setIdade}
                        placeholder="25"
                        placeholderTextColor={"#CCC"}
                        keyboardType="numeric"
                        maxLength={2}
                    />
                </View>
                <View style={style.containerInput}>
                    <Text style={style.label}>Possui convite?</Text>
                    <TextInput
                        style={style.input}
                        onChangeText={setConvite}
                        placeholder="1 para Sim, 0 para Não"
                        placeholderTextColor={"#CCC"}
                        keyboardType="numeric"
                        maxLength={1}
                    />
                </View>
                <View style={style.containerButton}>
                    <TouchableOpacity style={style.button} onPress={Verificar}>
                        <Text style={style.textButton}>Verificar</Text>
                    </TouchableOpacity>
                </View>
                { verificacao === 1 ? (
                    <View>
                        <Text style={style.message}>Tenha um excelente festival!</Text>
                        <Image source={happy} style={style.imageHappy}/>
                    </View>
                ) : verificacao === 0 ? (
                    <View>
                        <Text style={style.messageError}>Infelizmente você não pode entrar!</Text>
                        <Image source={sadness} style={style.imageSadness}/>
                    </View>
                ) : (<></>)}
            </View>
        </>
    )
}

const style = StyleSheet.create({
    container: {
        backgroundColor:'#f4F5F6',
        flex:1
    },
    test: {
        flexDirection:'row'   
        
    },
    containerHeader: {
        borderWidth:2,
        borderEndColor:'#343A40',
        borderBottomEndRadius:20,
        borderBottomStartRadius:20,
        paddingVertical:40,
        backgroundColor:'#DDD',
        flexDirection:'row',
        justifyContent:'space-around',
        alignItems:'center'
    },
    titleHeader :{
        color:'#343A40',
        fontSize:20,
        fontWeight:'bold',
        marginHorizontal:10,
        paddingVertical:20
    },
    imageRockInRio:{
        width:100,
        height:100,
        marginRight:20
    },
    description: {
        paddingHorizontal:30,
        color:'#343A40',
        fontSize:16,
        marginTop:40,
        textAlign:'center'
    },
    subDescription: {
        color:'#343A40',
        textAlign:'center',
        fontWeight:'bold',
        marginBottom:60,
    },
    and: {
        fontSize:18,
        color:'#DB4A2E'
    },
    containerInput: {
        paddingHorizontal:20,
        alignItems:'center'
    },
    label: {
        color:'#343A40',
        fontSize:16,
        fontWeight:'bold',
        marginBottom:10,
        textAlign:'center'
    },
    input: {
        borderWidth:1,
        borderColor:'#343A40',
        borderRadius:10,
        width:200,
        height:40,
        textAlign:'center',
        color:'#343A40',
        marginBottom:30,
    },
    containerButton: {
        alignItems:'center'
    },
    button: {
        width:150,
        height:40,
        borderWidth:1,
        borderColor:'#343A40',
        borderRadius:10,
        display:'flex',
        justifyContent:'center',
        alignItems:'center',
        backgroundColor:'#343A40'
    },
    textButton: {
        color:'#F4F5F6',
        fontWeight:'bold'

    },
    message: {
        marginTop:40,
        textAlign:'center',
        color:'black',
        fontSize:18,
        fontWeight:'bold'
    },
    messageError: {
        marginTop:40,
        textAlign:'center',
        color:'#DB4A2E',
        fontSize:18,
        fontWeight:'bold'
    },
    imageHappy:{
        width:140,
        height:120,
        alignSelf:'center',
        marginTop:15
    },
    imageSadness: {
        width:100,
        height:100,
        alignSelf:'center',
        marginTop:15
    }
});

export default HomeScreen
