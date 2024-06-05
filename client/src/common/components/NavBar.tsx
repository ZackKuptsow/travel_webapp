import Button from './Button'
import { BackgroundColorClasses, TextColorClasses } from '../enums'

const NavBar = () => {
    return (
        <nav className='p-8'>
            <div className='flex flex-row flex-auto justify-between'>
                <div className='flex'>
                    <a className='text-4xl text-terracotta' href="#">Free Agent</a>
                </div>
                <div className='flex justify-end space-x-4'>
                    <Button backgroundColor={BackgroundColorClasses.Transparent} fontColor={TextColorClasses.TextSteelBlue} redirectUrl='/activities' text='Activities' />
                    <Button backgroundColor={BackgroundColorClasses.Transparent} fontColor={TextColorClasses.TextSteelBlue} redirectUrl='/bites' text='Bites' />
                    <Button backgroundColor={BackgroundColorClasses.Transparent} fontColor={TextColorClasses.TextSteelBlue} redirectUrl='/stays' text='Stays' />
                    <Button backgroundColor={BackgroundColorClasses.Transparent} fontColor={TextColorClasses.TextSteelBlue} redirectUrl='/flights' text='Flights' />
                    <Button redirectUrl='/login' text='Login' />
                </div>
            </div>
        </nav>
    )
}

export default NavBar