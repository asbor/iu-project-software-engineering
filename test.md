| Title1           | Title2                                                                                                                                                    |
|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| First Normal Row | Small Data                                                                                                                                                |
| Second Long Row  | pandoc -s --metadata-file=pandoc-metadata-block.yml --from=markdown-markdown_in_html_blocks --lua-filter=parse-html.lua chapter1.md -o chapter1result.pdf |


# This is Chapter 1

<html>
<table>
    <col width="20%"/>
    <col width="20%"/>
    <col width="20%"/>
    <col width="30%"/>
    <tr>
        <th>Tipus d'activitat</th>
        <th>Objectius</th>
        <th>Verbs (principals)</th>
        <th>Actors</th>
    </tr>
    <tr>
        <td>3 actes</td>
        <td colspan=3>professor-classe, professor-grups <br> (es pot plantejar l'activitat en petits <br>
            grups de recolsament mutu)</td>
    </tr>
</table>
</html>

# Print HTML Command