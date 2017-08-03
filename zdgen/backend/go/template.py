template="""package zdesk

import (
	"errors"
	"fmt"
	"io/ioutil"
    "net/http"
)

func handle (resp *http.Response, err error) ([]byte, error) {{
	if err != nil {{
		return nil, err
	}}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {{
		return nil, err
	}}

	return body, nil
}}

{}
"""
