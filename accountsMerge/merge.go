// https://leetcode.com/problems/accounts-merge/description/
package accountsmerge

import "slices"

type account struct {
	name   string
	emails map[string]struct{}
}

func newAccount(name string, emails []string) account {
	set := make(map[string]struct{})
	for _, e := range emails {
		set[e] = struct{}{}
	}

	return account{name: name, emails: set}
}

func merge(og map[string]struct{}, emails []string) map[string]struct{} {
	for _, em := range emails {
		og[em] = struct{}{}
	}

	return og
}

func keys(m map[string]struct{}) []string {
	retv := make([]string, 0)
	for k := range m {
		retv = append(retv, k)
	}

	return retv
}

func accountsMerge(accounts [][]string) [][]string {
	acc := []account{}
	seen := map[string][]int{} // map of name to indexes in acc

	for i := 0; i < len(accounts); i++ {
		name := accounts[i][0]
		emails := accounts[i][1:]
		indexes, ok := seen[name]
		if !ok {
			acc = append(acc, newAccount(name, emails))
			seen[name] = []int{len(acc) - 1}
			continue
		}

		for _, idx := range indexes {
			curr := acc[idx]
			merged := false
			for _, email := range emails {
				if _, ok := curr.emails[email]; ok {
					curr.emails = merge(curr.emails, emails)
					merged = true
					break
				}
			}
			if !merged {
				acc = append(acc, newAccount(name, emails))
				seen[name] = append(seen[name], len(acc)-1)
			}
		}
	}

	retv := [][]string{}
	for _, acc := range acc {
		emails := keys(acc.emails)
		slices.Sort(emails)
		retv = append(retv, append([]string{acc.name}, emails...))
	}

	return retv
}
