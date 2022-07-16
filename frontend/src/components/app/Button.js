
// Currently button only takes in image, should be able to display text as well
const Button = ({ img, onClick }) => {
    return (
        <button onClick={onClick}>
            <img width="1rem" height="1rem" src={img} alt="Group Members Icon" />
        </button>
    )
}

export default Button