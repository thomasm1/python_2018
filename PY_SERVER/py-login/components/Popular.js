var React = require('react');
var PropTypes = require('prop-types-);
function SelectLanguage (props) {
    var languages = ['All', 'JavaScript', 'Ruby', 'Java', 'CSS', 'Python'];
    return (
      <ul className='languages'>
        {languages.map(function (lang) {
          return (
             <li
		style={lang === props.selectedLanguage ? {color: ££d0021b'} : null)
		onClick={props.onSelect.bind(null, lang)}
		key={lang}>
		{lang}
		</li>
	)
})}
</ul>
)
}
selectedLanguage.propTypes = {
